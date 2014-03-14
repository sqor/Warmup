#!/usr/bin/python
import os
import pyvows
import js_minimizer
import tempfile

@pyvows.Vows.batch
class Test_generate_combined_src_file(pyvows.Vows.Context):

    class CombinedFile(pyvows.Vows.Context):

        def setUp(self):
            self.test_src_files = []
            # generate src files to test against.
            for i in range(3):
                src_file = tempfile.mkstemp(dir='/var/tmp', suffix='.js')[1]
                self.test_src_files.append(src_file)

        def teardown(self):
            # remove those test files
            for src_file in self.test_src_files:
                os.remove(src_file)

        def topic(self):
            return js_minimizer.generate_combined_src_file(self.test_src_files)

        def exists(self, topic):
            pyvows.expect(os.path.exists(topic)).to_be_true()

        def is_named_correctly(self, topic):
            pyvows.expect(topic.startswith('compiled_')).to_be_true()
            pyvows.expect(topic.endswith('.js')).to_be_true()

        class Contents(pyvows.Vows.Context):
            def topic(self, parent_topic):
                return open(parent_topic, 'r').read()

            def are_correct(self, topic):
                pyvows.expect(topic).to_equal('')

