'use client';

interface InfoDialogProps {
  onClose: () => void;
}

export default function InfoDialog({ onClose }: InfoDialogProps) {
  return (
    <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0, 0, 0, 0.7)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
      <div style={{ backgroundColor: '#222', color: '#eee', padding: '2rem', borderRadius: '8px', width: '90%', maxWidth: '600px', maxHeight: '90vh', overflowY: 'auto' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', borderBottom: '1px solid #333', paddingBottom: '1rem', marginBottom: '1rem' }}>Metric Definitions</h2>
        
        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#0070f3' }}>Blood-Brain Barrier Safe</h3>
          <p style={{ color: '#aaa' }}>Reflects the DrugBank percentile of predicted blood–brain barrier penetration (BBB_Martins). Higher values indicate the compound behaves more similarly to approved drugs in terms of CNS exposure potential.</p>
          <p style={{ fontSize: '0.8rem', fontStyle: 'italic', color: '#888' }}>Based on: "BBB_Martins_drugbank_approved_percentile"</p>
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#0070f3' }}>hERG Safe</h3>
          <p style={{ color: '#aaa' }}>Represents the DrugBank percentile of predicted hERG channel inhibition risk. Higher scores suggest the compound aligns more closely with approved drugs regarding lower cardiotoxicity risk.</p>
          <p style={{ fontSize: '0.8rem', fontStyle: 'italic', color: '#888' }}>Based on: "hERG_drugbank_approved_percentile"</p>
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#0070f3' }}>Bioavailable</h3>
          <p style={{ color: '#aaa' }}>Based on the DrugBank percentile of predicted oral bioavailability (Bioavailability_Ma). Higher values indicate stronger similarity to approved drugs in terms of systemic absorption.</p>
          <p style={{ fontSize: '0.8rem', fontStyle: 'italic', color: '#888' }}>Based on: "Bioavailability_Ma_drugbank_approved_percentile"</p>
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#0070f3' }}>Soluble</h3>
          <p style={{ color: '#aaa' }}>Reflects the DrugBank percentile of predicted aqueous solubility (Solubility_AqSolDB). Higher scores suggest the compound’s solubility profile is more comparable to that of approved drugs.</p>
          <p style={{ fontSize: '0.8rem', fontStyle: 'italic', color: '#888' }}>Based on: "Solubility_AqSolDB_drugbank_approved_percentile"</p>
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#0070f3' }}>Non-Toxic</h3>
          <p style={{ color: '#aaa' }}>Calculated as the average DrugBank percentile across multiple toxicity-related predictions, including clinical toxicity, mutagenicity (AMES), drug-induced liver injury (DILI), carcinogenicity, and skin reaction. Higher values indicate overall toxicity characteristics more similar to those of approved drugs.</p>
          <p style={{ fontSize: '0.8rem', fontStyle: 'italic', color: '#888' }}>Based on the average of: "ClinTox_drugbank_approved_percentile", "AMES_drugbank_approved_percentile", "DILI_drugbank_approved_percentile", "Carcinogens_Lagunin_drugbank_approved_percentile", "Skin_Reaction_drugbank_approved_percentile"</p>
        </div>

        <p style={{ marginTop: '2rem', borderTop: '1px solid #333', paddingTop: '1rem' }}>
          Visit Here for More Information: 
          <a href="https://tdcommons.ai/single_pred_tasks/adme/" target="_blank" rel="noopener noreferrer" style={{ color: '#0070f3' }}> https://tdcommons.ai/single_pred_tasks/adme/</a>
        </p>

        <button onClick={onClose} style={{ marginTop: '2rem', padding: '0.5rem 1.5rem', width: '100%', border: 'none', borderRadius: '4px', backgroundColor: '#0070f3', color: '#fff', cursor: 'pointer' }}>Close</button>
      </div>
    </div>
  );
}
