'use strict';
import React from 'react';
import d3 from "d3";

import varScores from './mockdata/variants_to_funcscores';

import CollapsibleTile from "../collapsible/CollapsibleTile";
import CollapsibleSection from "../collapsible/CollapsibleSection";
import FuncClassSubtile from "./FuncClassSubtile";


export const impacts = [
    { range: [-Infinity, -1.328], label: "Loss of Function", color: '#fc0d1b' },
    { range: [-1.328, -0.748], label: "Uncertain", color: '#fee49d' },
    { range: [-0.748, Infinity], label: "No Functional Impact", color: '#0f0' }
];

export default class FunctionalAssayTile extends React.Component {
    render() {
        const funcScore = varScores[this.props['HGVS_cDNA']];

        const impactScale = d3.scale.threshold()
            .domain(impacts[1].range)
            .range(impacts);

        if (funcScore === undefined) {
            return (
                <CollapsibleTile allEmpty={true} {...this.props}>
                    <div style={{padding: '10px'}}>
                    No functional assay data exists for this variant.
                    </div>
                </CollapsibleTile>
            );
        }

        return (
            <CollapsibleTile allEmpty={false} {...this.props}>
                <CollapsibleSection
                    fieldName="Findlay Function Score"
                    extraHeaderItems={<span>Score: {funcScore} ({impactScale(funcScore).label})</span>}
                    defaultVisible={true}
                >
                    <div className="subtile-container" style={{padding: 20, paddingTop: 10, paddingBottom: 10}}>
                    This histogram summarizes functional classification results from saturation genome editing, provided by the Starita lab at the University of Washington (<a href="https://www.ncbi.nlm.nih.gov/pubmed/30209399">Findlay et al, Nature, 2018</a>). Please see <a href="https://sge.gs.washington.edu/BRCA1/">their site</a> for further information.
                    </div>

                    <div id="func-assay-container" style={{textAlign: 'center'}}>
                        <FuncClassSubtile score={funcScore} impactScale={impactScale} />
                    </div>

                    <div style={{padding: 20, paddingTop: 10, fontSize: 'smaller', fontStyle: 'italic', textAlign: 'center'}}>
                        The median synonymous SNV scored 0.0 and the median nonsense SNV scored -2.12.
                    </div>
                </CollapsibleSection>
            </CollapsibleTile>
        );
    }
}
