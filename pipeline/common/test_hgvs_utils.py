"""
A few integration tests
"""

import pytest
from common import hgvs_utils
from common.variant_utils import VCFVariant


@pytest.fixture()
def wrapper():
    return hgvs_utils.HgvsWrapper()


@pytest.fixture()
def hgvs_variant(wrapper):
    return (VCFVariant.from_str('chr13:g.32316477:AAG>A').
            to_hgvs_obj(wrapper.contig_maps[hgvs_utils.HgvsWrapper.GRCh38_Assem]))


def test_to_cdna(wrapper, hgvs_variant):
    cdna = wrapper.to_cdna(hgvs_variant)
    assert str(cdna) == 'NM_000059.3:c.17_19delinsA' # normalized 'NM_000059.3:c.22_23del'


def test_to_protein(wrapper, hgvs_variant):
    protein = wrapper.to_protein(wrapper.to_cdna(hgvs_variant))
    assert str(protein) == 'NP_000050.2:p.(Arg8AlafsTer5)'


def test_normalize(wrapper, hgvs_variant):
    obj = wrapper.normalizing(hgvs_variant)
    assert str(obj) == 'NC_000013.11:g.32316482_32316483del'


def test_hg19_to_hg38(wrapper):
    vars38 = ['chr13:g.32316477:AAG>A', 'chr17:g.43079204:A>C', 'chr17:g.43053755:G>A', 'chr17:g.43125273:T>C',
              None] # outside transcript boundaries
    vars37 = ['chr13:g.32890614:AAG>A', 'chr17:g.41231221:A>C', 'chr17:g.41205772:G>A', 'chr17:g.41277290:T>C',
              'chr17:g.41279883:GAC>G']

    for (v37, v38) in zip(vars37, vars38):
        v37_obj = VCFVariant.from_str(v37).to_hgvs_obj(wrapper.contig_maps[hgvs_utils.HgvsWrapper.GRCh37_Assem])

        if v38:
            v38_obj = VCFVariant.from_hgvs_obj(wrapper.hg19_to_hg38(v37_obj))
            assert VCFVariant.from_str(v38) == v38_obj
        else:
            with pytest.raises(ValueError):
                wrapper.hg19_to_hg38(v37_obj)

