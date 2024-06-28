/*
A KBase module: dpvs2004bedtools_bamtofastq
*/

module dpvs2004bedtools_bamtofastq {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_dpvs2004bedtools_bamtofastq(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
