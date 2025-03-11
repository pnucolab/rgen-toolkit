VarCas-OFFinder
===============

**VarCas-OFFinder** is a variant aware potential off-target site identifying tool 
based on Cas-OFFinder. Using a reference genome alone to search potential off-target sites
has many drawbacks since it may not contain individual variants, making it challenging for
therapeutic applications. VarCas-OFFinder considers individual variants along with 
reference genome to search potential off-target sites. 

Quick Start to use the web interface
------------------------------------

1. Navigate to https://crispr.pnucolab.com/
2. Download the provided **Sample VCF file**
3. Default settings:

   - Target Genome: Homo sapiens (GRCh38/hg38)
   - PAM Type: SpCas9 from Streptococcus pyogenes: 5'-NRG-3'
   - Query Sequence: CAGCAACTCCAGGGGGCCGC
   - Mismatches: 3

4. Click Submit to process the sample file.
5. For custom analysis, upload your phased single-sample VCF file.
6. For faster execution, upload a VCF file containing a few chromosomes, like chr1 and chr2, by filtering them using the command:

   .. code-block:: bash

      bcftools view -r chr6,chr10 NA12878.vcf.gz -o Output.vcf.gz


Check out the :doc:`usage` section for further information.





.. toctree::
   :maxdepth: 4
   :caption: Contents


   cli
   usage
   deploy
   webtool

