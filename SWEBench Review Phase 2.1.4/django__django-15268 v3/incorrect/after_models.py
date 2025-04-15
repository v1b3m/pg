@@ -540,6 +540,7 @@ class AlterUniqueTogether(AlterTogetherOptionOperation):
        super().__init__(name, unique_together)



class AlterIndexTogether(AlterTogetherOptionOperation):
    """
    Change the value of index_together to the target one.