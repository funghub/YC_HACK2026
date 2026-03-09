'use client';

interface HeatmapInfoDialogProps {
  onClose: () => void;
}

export default function HeatmapInfoDialog({ onClose }: HeatmapInfoDialogProps) {
  return (
    <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0, 0, 0, 0.7)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
      <div style={{ backgroundColor: '#222', color: '#eee', padding: '2rem', borderRadius: '8px', width: '90%', maxWidth: '600px', maxHeight: '90vh', overflowY: 'auto' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', borderBottom: '1px solid #333', paddingBottom: '1rem', marginBottom: '1rem' }}>How to Read the Heatmap</h2>
        <p style={{ color: '#aaa', lineHeight: 1.6 }}>
          In this heatmap, red indicates a high, favorable score, while blue represents a low, poor score. You are looking at three critical performance metrics: RMSD (where lower values are normalized to show higher accuracy), the Score (a geometric mean of normalized RMSD and pLDDT, balancing structural precision with model confidence), and the Success Rate (the frequency of high-quality predictions meeting the threshold of RMSD &lt; 2.0Å and lDDT &gt; 0.8). By scanning for clusters of red, you can quickly identify which experimental conditions produce the most reliable, high-resolution models, while blue areas highlight potential structural failures or low-confidence predictions that may require optimization.
        </p>
        <button onClick={onClose} style={{ marginTop: '2rem', padding: '0.5rem 1.5rem', width: '100%', border: 'none', borderRadius: '4px', backgroundColor: '#0070f3', color: '#fff', cursor: 'pointer' }}>Close</button>
      </div>
    </div>
  );
}
