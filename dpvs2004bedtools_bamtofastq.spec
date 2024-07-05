/*
A KBase module: dpvs2004bedtools_bamtofastq
*/

module dpvs2004bedtools_bamtofastq {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        An app that takes a bam file and converts it into fastq
    */
    funcdef run_dpvs2004bedtools_bamtofastq(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
