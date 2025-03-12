

How to use the command-line interface
=====================================

Cas-OFFinder is built upon OpenCL to identify potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.

Create your environment:

.. code-block:: bash

    conda create -n crispr

Download requirements.txt and vcf-cas-offinder.py from the command-line interface directory and install all dependencies using the command:

.. code-block:: bash

   pip install —no-cache-dir -r requirements.txt

Download the Cas-OFFinder binary file from https://github.com/pnucolab/VarCas-OFFinder/raw/refs/heads/main/backend/cas-offinder 
in the same directory with vcf-cas-offinder.py. 

Install the vcflib package using conda, execute the following command:

.. code-block:: bash

   conda install -c bioconda vcflib=1.0.3 tabixpp=1.1.0

Download the chromosome FASTA files for any target organism. You can find one using the links below, or you can use any other sources.

- For Vertebrates

.. code-block:: bash
   
    https://ftp.ensembl.org/pub/
 
- For Plants

.. code-block:: bash
                
   https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/

Extract all FASTA files into a directory. Index the extracted reference genome within the same directory

.. code-block:: bash
        
   samtools faidx ref.genome # replace ref.genome with tha actual name of the extracted reference genome 

Ensure that the “+x” flag is added to the input_vcf_file and the target organism’s reference genome directory.
Now, the Allelic Cas-OFFinder pipeline can run with:

.. code-block:: bash
        
   ./vcf-cas-offinder.py -i input_vcf_file_path -r reference_genome_path -t target_sequence_input_file_name -d device_id 

For device_id, you can use G, C, or A
   - G represents using GPU devices, while C stands for CPUs. A represents accelerators. 
   - If you have multiple GPU or CPU IDs, you can specify them as G0 for GPU device ID 0 and G1 for ID 1 to limit the number of devices used. 

For a short help, try running:

.. code-block:: bash
        
          ./vcf-cas-offinder.py -h 

.. code-block:: bash
        
   usage: vcf-cas-offinder.py [-h] -i INPUT -r REF_PATH -t QUERY_INPUT -d DEVICE_ID

   Identify potential off-target sites based on VCF files.

   options:
   -h, --help            show this help message and exit
   -i INPUT, --input INPUT
                        Path to the input VCF (Phased and single sample) file
   -r REF_PATH, --ref_path REF_PATH
                        Path to the target organism reference genome
   -t QUERY_INPUT, --query_input QUERY_INPUT
                        target sequence in the target organism genome (input.txt file)
   -d DEVICE_ID, --device_id DEVICE_ID
                        device_id(s): C for CPU and G for GPU, G0 for GPU device id=0

You should create an input.txt file in the same directory with vcf-cas-offinder. 
An example of an input file:

.. code-block:: bash
        
      NNNNNNNNNNNNNNNNNNNNGG
      GTGAAATCTAAGTGTAGAGNNN 2
      TTGTGAAATCTAAGTGTAGNNN 2
      CTTCACAATTATTCGCCCANNN 2
      GGGCGAATAATTGTGAAGGNNN 2
      CTTACAGAAACACCTGTTANNN 2
      AGATTCAAGAATTGGTACGNNN 2
      AACCTTCAGTTAGTCGCTANNN 2
      CACCATAGCGACTAACTGANNN 2
      AGCTCAGGAAGGCCCTCATNNN 2

- The first line indicates the desired pattern, including the PAM site.
- The remaining lines are the query sequences and maximum mismatch numbers, separated by spaces.
- The length of the desired pattern and the query sequences should be the same.

Now you can run allelic-Cas-OFFinder as follows (using GPUs):

.. code-block:: bash
        
      ./allelic-cas-offinder.py -i /home/user/Documents/vcf_files/bgzipresultcm334.vcf.gz -r /home/user/genome/pepper_ref/GCA_000512255.2_ASM51225v2_genomic.fa -t input.txt -d G1


Sample results can be obtained fro  https://github.com/pnucolab/VarCas-OFFinder/blob/main/docs_old/images/Screenshot%202025-03-07%20231028.png. 

- 0 after the colon in the second column represents allele 1, and 1 represents allele 2 for each chromosome. In the example shown above, CVCM334_CM008455, CVCM334_CM008456, etc, are chromosome identifiers found in the allelic fasta files. 



