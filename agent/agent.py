import json  # Still useful for printing/debugging args
import os

import google.generativeai as genai
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from google.generativeai.types import HarmBlockThreshold, HarmCategory

# --- Configuration ---
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

genai.configure(api_key=google_api_key)

# Choose a Gemini model
# gemini-1.5-pro-latest is generally more capable, especially with function calling
MODEL_NAME = "gemini-1.5-pro-latest"
# MODEL_NAME = "gemini-pro" # Less capable, but might work for simpler tasks


# --- Tool Definition (Python Function - Remains the same) ---
def perform_web_search(query: str, num_results: int = 3) -> str:
    """Performs a web search using DuckDuckGo and returns summarized results."""
    print(f"--- Tool: Performing web search for '{query}' ---")
    try:
        with DDGS() as ddgs:
            # Using .text() which returns dictionaries with 'title', 'body', 'href'
            results = list(ddgs.text(query, max_results=num_results))
            if not results:
                return "No results found."
            # Format results for the LLM
            formatted_results = "\n".join(
                [
                    f"Title: {r['title']}\nSnippet: {r['body']}\nURL: {r['href']}\n---"
                    for r in results
                ]
            )
            print(f"--- Tool: Found {len(results)} results ---")
            # Return a limited amount of text to avoid exceeding context limits
            return formatted_results[:3000]  # Gemini can handle larger context
    except Exception as e:
        print(f"--- Tool: Error during search: {e} ---")
        return f"Error performing search: {e}"


# --- Tool Definition (For Google API) ---
# Describe the tool structure for the Google API
# This tells the model *how* to ask for the tool to be called
web_search_tool = genai.protos.Tool(
    function_declarations=[
        genai.protos.FunctionDeclaration(
            name="perform_web_search",
            description="Searches the web using DuckDuckGo to find current information, facts, or answers to questions that require up-to-date knowledge beyond the LLM's training data. Use this for specific facts, recent events, or detailed information.",
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    "query": genai.protos.Schema(
                        type=genai.protos.Type.STRING,
                        description="The search query to use.",
                    )
                },
                required=["query"],
            ),
        )
    ]
)

# Map tool names to actual Python functions
AVAILABLE_TOOLS = {"perform_web_search": perform_web_search}

# --- Core Agent Logic ---


def run_agent(user_goal: str, max_iterations: int = 5):
    """Runs the Gemini-powered agent loop."""
    print(f"\n--- Agent Starting (using Google Gemini: {MODEL_NAME}) ---")
    print(f"Goal: {user_goal}")

    # Configure the generative model
    model = genai.GenerativeModel(
        MODEL_NAME,
        # Define tools the model can use
        tools=[web_search_tool],
        # Safety settings - Adjust as needed, can be sensitive
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        # System instruction (optional, helps guide the model)
        # Note: Official 'system' role support varies; putting instructions here is common
        system_instruction="""You are an AI assistant designed to achieve goals by reasoning and using available tools when necessary.
Your task is to fulfill the user's request.
1. Analyze the request.
2. If you can answer directly, provide the final answer prefixed with 'FINAL_ANSWER:'.
3. If you need external information, call the appropriate function ('perform_web_search').
4. Use the function results to formulate your final answer, prefixed with 'FINAL_ANSWER:'.
5. If you encounter issues or cannot fulfill the request, state that in the final answer.""",
    )

    # Start a chat session (maintains history)
    chat = model.start_chat(
        enable_automatic_function_calling=False
    )  # We handle function calling manually

    # Initial prompt including the goal
    prompt = f"My goal is: {user_goal}"

    for i in range(max_iterations):
        print(f"\n--- Iteration {i+1} ---")
        print("Agent: Sending prompt/data to LLM...")
        # print(f"Current Prompt/History Context for LLM:\n{prompt}") # Debugging

        try:
            # Send the prompt (or function response) to the model
            response = chat.send_message(prompt)
            # print(f"LLM Raw Response Parts: {response.parts}") # Debugging

            # Check for function call
            if response.parts[0].function_call.name:
                fc = response.parts[0].function_call
                tool_name = fc.name
                tool_args = {
                    key: value for key, value in fc.args.items()
                }  # Convert Struct to dict

                print(
                    f"Agent: LLM requests tool '{tool_name}' with args: {json.dumps(tool_args)}"
                )

                if tool_name in AVAILABLE_TOOLS:
                    # Call the actual Python function
                    tool_function = AVAILABLE_TOOLS[tool_name]
                    try:
                        tool_result = tool_function(**tool_args)
                    except Exception as e:
                        print(f"--- Tool Execution Error: {e} ---")
                        tool_result = f"Error executing tool {tool_name}: {e}"

                    print("Agent: Received tool result.")
                    # Prepare the function response *part* to send back to the model
                    prompt = genai.protos.Part(
                        function_response=genai.protos.FunctionResponse(
                            name=tool_name,
                            response={
                                "result": tool_result
                            },  # Structure the response as expected
                        )
                    )
                else:
                    print(f"Agent: LLM requested unknown tool '{tool_name}'")
                    # Inform the model the tool is unknown
                    prompt = genai.protos.Part(
                        function_response=genai.protos.FunctionResponse(
                            name=tool_name,
                            response={
                                "error": f"Unknown tool '{tool_name}'. Available tools: {list(AVAILABLE_TOOLS.keys())}"
                            },
                        )
                    )

            # Check for final answer in text response
            elif response.parts[0].text:
                text_response = response.parts[0].text
                print("Agent: Received text response from LLM.")
                # print(f"LLM Text: {text_response}") # Debugging
                if text_response.strip().startswith("FINAL_ANSWER:"):
                    final_answer = (
                        text_response.strip().replace("FINAL_ANSWER:", "").strip()
                    )
                    print("\n--- Agent Finished ---")
                    print(f"Final Answer: {final_answer}")
                    return final_answer
                else:
                    # If it's not a final answer, treat it as intermediate reasoning
                    # or potentially a direct answer if the model skipped the prefix (less ideal)
                    # We'll let the loop continue, sending this text back might confuse it,
                    # better to just prompt again if needed, or handle this case more explicitly
                    # For this simple agent, assume if it's not a tool call or FINAL_ANSWER, it might be stuck
                    # or thinks it *has* answered. We could just return the text here.
                    print(
                        "Agent: Received text response, but not marked as FINAL_ANSWER. Assuming it's the answer (or intermediate reasoning)."
                    )
                    print("\n--- Agent Finished (potentially incomplete) ---")
                    print(f"Response: {text_response}")
                    return text_response  # Return the text directly

            else:
                # Should not happen if model behaves correctly (either text or function call)
                print("Agent: Received unexpected response format from LLM.")
                prompt = "Please respond with either a function call or text prefixed with FINAL_ANSWER:."

        except Exception as e:
            print(f"An error occurred during LLM interaction: {e}")
            # Check for specific content blocking
            if "response was blocked" in str(e):
                print(
                    "Error Details: Response may have been blocked due to safety settings."
                )
                try:
                    print(f"Prompt Feedback: {response.prompt_feedback}")
                except Exception:
                    pass  # Might not have feedback if error was earlier
            return "Agent failed due to an error."

    print("\n--- Agent Finished (Max Iterations Reached) ---")
    return "Agent could not reach a final answer within the iteration limit."


# --- Run the Agent ---
if __name__ == "__main__":
    # user_question = "What is the capital of France?" # Simple, LLM should know
    user_question = "Why are we here?"  # Requires recent info -> tool use
    # user_question = "Summarize the main points of the Wikipedia page for 'Artificial General Intelligence'." # Requires reading external content via search

    run_agent(user_question)
