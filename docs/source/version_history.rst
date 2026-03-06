Version History
===============

.. contents::
    :local:
    :depth: 2

1.x Series
----------

1.0.1
~~~~~

**Performance**

- **Optimized vcf2fasta Pipeline**: Substantially reduced execution time for
  variant-to-sequence conversion, enabling more efficient processing of
  large-scale VCF datasets.
- **Polyploid Genome Support**: Extended compatibility to handle polyploid
  genomes, enabling analysis for a wider range of organisms.

**User Interface**

- **Empty VCF Warning**: Users now receive a clear warning when uploading
  empty VCF files, preventing confusion and wasted processing time.
- **Configurable Result Display**: Expanded rows-per-page options allow users
  to tailor the display density to their workflow and dataset size.

**New Features**

- **Chromosome-level Summary Table**: New summary table displays total
  off-target sites per chromosome with allele-specific counts for each gRNA.
- **Advanced Result Filtering**: Filter results by gRNA sequence, mismatch
  count, and GC content for more targeted analysis.

1.0.0
~~~~~

- Initial public release of Variant-aware Cas-OFFinder — a variant-aware
  off-target prediction tool that incorporates individual genetic variants
  (via VCF files) alongside reference genomes.
- Support for 40+ PAM types.
- Unlimited mismatch tolerance for comprehensive off-target site detection.
