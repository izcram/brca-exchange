import pytest
import unittest
import aggregate_across_columns


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.newRow = {
            'Variant_frequency_LOVD': '',
            'ClinVarAccession_ENIGMA': '-',
            'BX_ID_ExAC': '-',
            'Chr': '13',
            'Protein_Change': '-',
            'BIC_Nomenclature_exLOVD': '-',
            'Co_occurrence_LR_exLOVD': '-',
            'Reference_Sequence': 'NM_000059.3',
            'Submitter_ClinVar': 'Sharing_Clinical_Reports_Project_(SCRP),GeneDx,Breast_Cancer_Information_Core_(BIC)_(BRCA2)',
            'Submitters_LOVD': 'Genevieve Michils (Leuven,BE)',
            'Clinical_classification_BIC': 'Pending',
            'Method_ClinVar': 'clinical_testing',
            'Pathogenicity_all': 'Benign,Likely_benign,Uncertain_significance (ClinVar); Pending (BIC)',
            'Germline_or_Somatic_BIC': 'G',
            'BIC_Nomenclature': 'IVS1-12delTCT',
            'Clinical_significance_citations_ENIGMA': '-',
            'Collection_method_ENIGMA': '-',
            'Sum_family_LR_exLOVD': '-',
            'HGVS_cDNA_LOVD': 'NM_000059.3:c.-39-12_-39-10del',
            'EAS_Allele_frequency_1000_Genomes': '-',
            'Ethnicity_BIC': 'Western European,Caucasian,None Specified',
            'Individuals_LOVD': '1',
            'polyPhen2_result_ESP': 'None',
            'URL_ENIGMA': '-',
            'BX_ID_exLOVD': '-',
            'Allele_Origin_ClinVar': 'germline',
            'AFR_Allele_frequency_1000_Genomes': '-',
            'EUR_Allele_frequency_1000_Genomes': '-',
            'Source': 'ClinVar,LOVD,ESP,BIC',
            'Condition_ID_value_ENIGMA': '-',
            'HGVS_Protein': 'p.(?)',
            'Ref': 'TTCT',
            'Sift_Prediction': '-',
            'BX_ID_LOVD': '11',
            'Gene_Symbol': 'BRCA2',
            'Comment_on_clinical_significance_ENIGMA': '-',
            'Missense_analysis_prior_probability_exLOVD': '-',
            'Assertion_method_ENIGMA': '-',
            'Posterior_probability_exLOVD': '-',
            'Polyphen_Score': '-',
            'Hg38_End': 32316412, 'HGVS_cDNA': 'c.-39-12_-39-10delTCT',
            'SAS_Allele_frequency_1000_Genomes': '-',
            'RNA_LOVD': 'r.(?)',
            'BX_ID_1000_Genomes': '-',
            'BX_ID_ClinVar': '31,30,29',
            'IARC_class_exLOVD': '-',
            'BX_ID_BIC': '1,3,2,5,4,7,6',
            'Allele_origin_ENIGMA': '-',
            'Date_last_evaluated_ENIGMA': '-',
            'HGVS_ClinVar': 'NM_000059.3.c.-39-12_-39-10delTCT',
            'BIC_Designation_BIC': 'IVS1-12delTCT',
            'Date_Last_Updated_ClinVar': '2017-03-03,2002-05-29,2010-12-17',
            'Hg38_Start': '32316409',
            'SCV_ClinVar': 'SCV000053901,SCV000145913,SCV000569168',
            'Pathogenicity_expert': 'Not Yet Reviewed',
            'Allele_frequency_1000_Genomes': '-',
            'Combined_prior_probablility_exLOVD': '-',
            'AMR_Allele_frequency_1000_Genomes': '-',
            'Condition_category_ENIGMA': '-',
            'BX_ID_ESP': '1',
            'Patient_nationality_BIC': 'Italy (both sides),-,Italian',
            'Genetic_origin_LOVD': 'Unknown',
            'Number_of_family_member_carrying_mutation_BIC': '-',
            'Genomic_Coordinate_hg38': 'chr13:g.32316410:TCT>-,chr13:g.32316406:GTCT>G',
            'Allele_frequency_ExAC': '-',
            'Mutation_type_BIC': 'IVS',
            'Assertion_method_citation_ENIGMA': '-',
            'Condition_ID_type_ENIGMA': '-',
            'HGVS_protein_LOVD': 'p.(?)',
            'Clinical_importance_BIC': 'unknown',
            'HGVS_cDNA_exLOVD': '-',
            'Clinical_significance_ENIGMA': '-',
            'Minor_allele_frequency_ESP': '0.2181,0.0704,0.1678',
            'Segregation_LR_exLOVD': '-',
            'Clinical_Significance_ClinVar': 'Benign,Likely_benign,Uncertain_significance',
            'BX_ID_ENIGMA': '-',
            'HGVS_RNA': '-',
            'Literature_source_exLOVD': '-',
            'Variant_effect_LOVD': '?/?',
            'Polyphen_Prediction': '-',
            'Protein_ClinVar': 'None',
            'Literature_citation_BIC': '-',
            'Pos': '32316409',
            'HGVS_protein_exLOVD': '-',
            'Sift_Score': '-',
            'Alt': 'T'
        }

    def test_break_up_esp_allele_frequencies(self):
        self.newRow["Minor_allele_frequency_ESP"] = '0.2181,0.0704,0.1678'
        (eaAlleleFrequency, aaAlleleFrequency, alleleFrequency) = aggregate_across_columns.breakUpESPAlleleFrequencies(self.newRow)
        self.assertEqual(eaAlleleFrequency, (float(0.2181) / 100))
        self.assertEqual(aaAlleleFrequency, (float(0.0704) / 100))
        self.assertEqual(alleleFrequency, (float(0.1678) / 100))

        self.newRow["Minor_allele_frequency_ESP"] = '-'
        (eaAlleleFrequency, aaAlleleFrequency, alleleFrequency) = aggregate_across_columns.breakUpESPAlleleFrequencies(self.newRow)
        self.assertEqual(eaAlleleFrequency, '-')
        self.assertEqual(aaAlleleFrequency, '-')
        self.assertEqual(alleleFrequency, '-')

        self.newRow["Minor_allele_frequency_ESP"] = None
        (eaAlleleFrequency, aaAlleleFrequency, alleleFrequency) = aggregate_across_columns.breakUpESPAlleleFrequencies(self.newRow)
        self.assertEqual(eaAlleleFrequency, '-')
        self.assertEqual(aaAlleleFrequency, '-')
        self.assertEqual(alleleFrequency, '-')

        self.newRow["Minor_allele_frequency_ESP"] = '0.2181'
        (eaAlleleFrequency, aaAlleleFrequency, alleleFrequency) = aggregate_across_columns.breakUpESPAlleleFrequencies(self.newRow)
        self.assertEqual(eaAlleleFrequency, (float(0.2181) / 100))
        self.assertEqual(aaAlleleFrequency, '-')
        self.assertEqual(alleleFrequency, '-')


if __name__ == '__main__':
    pass
