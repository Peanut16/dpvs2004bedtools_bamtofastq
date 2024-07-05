# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import subprocess

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class dpvs2004bedtools_bamtofastq:
    '''
    Module Name:
    dpvs2004bedtools_bamtofastq

    Module Description:
    A KBase module: dpvs2004bedtools_bamtofastq
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/Peanut16/dpvs2004bedtools_bamtofastq.git"
    GIT_COMMIT_HASH = "7be5c4dc4d83c12c2435f47e57cd2e8a4303f523"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_dpvs2004bedtools_bamtofastq(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_dpvs2004bedtools_bamtofastq
        #for name in ['file_type', 'workspace_name']:
        #    if name not in params:
        #        raise ValueError('Parameter "' + name + '" is required but missing')
        #for option in ['dropdown_options']:
        #    if option['value'] != option['file_type']:
        #        raise ValueError('It must be a BAM file')
        
        #report = KBaseReport(self.callback_url)
        #report_info = report.create({'report': {'objects_created':[],
        #                                        'text_message': params['filename_end2.fq']},
        #                                        'workspace_name': params['workspace_name']})
        
        bam_filename = params['bam_file']
        with open(bam_filename, 'rb') as file:
            bam_data = file.read().decode('utf-8', 'ignore')
        print(bam_data)
        open('filename_end1.fq', 'w').close()
        open('filename_end2.fq', 'w').close()
        with open('filename_end2.fq', 'w') as f:
            result = subprocess.Popen(['bedtools', 'bamtofastq', '-i', bam_filename, '-fq', 
                                       'filename_end1.fq', '-fq2', '/dev/stdout'], stdout=f)

        #output = {
        #    'report_name': report_info['name'],
        #    'report_ref': report_info['ref'],
        #}

        output = {}

        #END run_dpvs2004bedtools_bamtofastq

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_dpvs2004bedtools_bamtofastq return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def run_dpvs2004bedtools_bamtofastq(self, ctx, params):
        """
        New app which takes a bam file and converts it into a fastq file
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run-dpvs2004bedtools_bamtofastq
        #END run-dpvs2004bedtools_bamtofastq

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run-dpvs2004bedtools_bamtofastq return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
