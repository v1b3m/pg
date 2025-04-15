@@ -335,10 +335,9 @@ class DeletionTests(TestCase):
        batch_size = connection.ops.bulk_batch_size(['pk'], objs)
        # The related fetches are done in batches.
        batches = ceil(len(objs) / batch_size)
        # One query for Avatar.objects.all() and one related fast delete combined and
        # then deletion of Avatar objects in batches of GET_ITERATOR_CHUNK_SIZE.
        fetches_to_mem = 1 + 1
        queries = fetches_to_mem + TEST_SIZE // GET_ITERATOR_CHUNK_SIZE
        self.assertNumQueries(queries, Avatar.objects.all().delete)
        self.assertFalse(Avatar.objects.exists())
@@ -355,8 +354,9 @@ class DeletionTests(TestCase):
        # + 1 (select related `U` instances)
        # + TEST_SIZE / GET_ITERATOR_CHUNK_SIZE (delete `T` instances in batches)
        # + 1 (delete `s`)
        # One query to select related `T` instances, one query to fast delete related `U` instances,
        # then deletion of `T` instances in batches, and one query to delete `s`.
        expected_num_queries = 1 + ceil(TEST_SIZE / GET_ITERATOR_CHUNK_SIZE) + 2

        self.assertNumQueries(expected_num_queries, s.delete)
        self.assertFalse(S.objects.exists())