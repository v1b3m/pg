        batch_size = connection.ops.bulk_batch_size(['pk'], objs)
        # The related fetches are done in batches.
        batches = ceil(len(objs) / batch_size)
        # One query for Avatar.objects.all() and then one related fast delete for
        # each batch.
        fetches_to_mem = 1 + batches
        # The Avatar objects are going to be deleted in batches of GET_ITERATOR_CHUNK_SIZE
        queries = fetches_to_mem + TEST_SIZE // GET_ITERATOR_CHUNK_SIZE
        self.assertNumQueries(queries, Avatar.objects.all().delete)
        self.assertFalse(Avatar.objects.exists())
        # + 1 (select related `U` instances)
        # + TEST_SIZE / GET_ITERATOR_CHUNK_SIZE (delete `T` instances in batches)
        # + 1 (delete `s`)
        expected_num_queries = ceil(TEST_SIZE / batch_size)
        expected_num_queries += ceil(TEST_SIZE / GET_ITERATOR_CHUNK_SIZE) + 2

        self.assertNumQueries(expected_num_queries, s.delete)
        self.assertFalse(S.objects.exists())