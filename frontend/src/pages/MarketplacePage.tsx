import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { extensionsApi } from '../api/client';
import type { Extension } from '../types';

function MarketplacePage() {
  // State hooks - like variables that trigger re-renders when changed
  const [extensions, setExtensions] = useState<Extension[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Effect hook - runs when component mounts (like componentDidMount in classes)
  useEffect(() => {
    const fetchExtensions = async () => {
      try {
        const data = await extensionsApi.list();
        setExtensions(data.filter(ext => ext.status === 'approved'));
        setLoading(false);
      } catch (err) {
        setError('Failed to load extensions');
        setLoading(false);
      }
    };

    fetchExtensions();
  }, []); // Empty array = run once on mount

  if (loading) return <div>Loading extensions...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="marketplace">
      <h2>Browse Extensions</h2>
      <div className="extensions-grid">
        {extensions.map(ext => (
          <div key={ext.id} className="extension-card">
            <h3>{ext.name}</h3>
            <p>{ext.description}</p>
            <p>Version: {ext.version} | Downloads: {ext.downloads}</p>
            <p>By: {ext.developer.username}</p>
            <Link to={`/extension/${ext.id}`}>View Details</Link>
          </div>
        ))}
      </div>
      {extensions.length === 0 && <p>No extensions available yet.</p>}
    </div>
  );
}

export default MarketplacePage;
