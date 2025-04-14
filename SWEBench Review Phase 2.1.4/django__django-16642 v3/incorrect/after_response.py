@@ -608,14 +608,15 @@ class FileResponse(StreamingHttpResponse):
                content_type, encoding = mimetypes.guess_type(filename)
                # Encoding isn't set to prevent browsers from automatically
                # uncompressing files.
                mapping = {
                    "bzip2": "application/x-bzip",
                    "gzip": "application/gzip",
                    "xz": "application/x-xz",
                    "compress": "application/x-compress",
                    "br": "application/brotli",
                }
                content_type = mapping.get(encoding, content_type)
                self.headers["Content-Type"] = content_type or "application/octet-stream"
            else:
                self.headers["Content-Type"] = "application/octet-stream"
