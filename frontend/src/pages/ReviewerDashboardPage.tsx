import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import type { Extension } from '../types';
import { extensionsApi } from '../api/client';

function ReviewDashboardPage() {
  const [pendingExtensions, setPendingExtensions] = useState<Extension[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);


  useEffect(() => {
    const fetchPending = async () => {
      try {
        const data = await extensionsApi.getPending();
        setPendingExtensions(data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load pending extensions');
        setLoading(false);
      }
    };

    fetchPending();
  }, [])

  if (loading) return <div>Loading pending reviews...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="reviewer-dashboard">
      <h2>Reviewer Dashboard</h2>
      <p>Pending extensions awaiting review: {pendingExtensions?.length ?? 0}</p>

      <div className="pending-queue">
        {pendingExtensions && pendingExtensions.map(ext => (
          <div key={ext.id} className="review-card">
            <h3>{ext.name} v{ext.version}</h3>
            <p>{ext.description}</p>
            <p>Submitted by: {ext.developer.username}</p>
            <p>Status: <strong>{ext.status}</strong></p>
            <p>Flags: {ext.flags?.length ?? 0}</p>
            <div className="review-actions">
              <Link to={`/extension/${ext.id}`}>View Details</Link>
              <button>Approve</button>
              <button>Reject</button>
            </div>
          </div>
        ))}
      </div>

      {pendingExtensions.length === 0 && (
        <p>No extensions pending review. Great job!</p>
      )}
    </div>
  );
}

export default ReviewDashboardPage;
