import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { extensionsApi } from '../api/client';

function SubmitExtensionPage() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData(e.currentTarget);

    try {
      await extensionsApi.create(formData);
      alert('Extension submitted successfully! It will be reviewed shortly.');
      navigate('/');
    } catch (err) {
      setError('Failed to submit extension. Please try again.');
      setLoading(false);
    }
  };

  return (
    <div className="submit-extension">
      <h2>Submit Your Extension</h2>
      <p>Upload your extension for review</p>

      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Extension Name:</label>
          <input type="text" id="name" name="name" required />
        </div>

        <div>
          <label htmlFor="slug">Slug (URL-friendly name):</label>
          <input type="text" id="slug" name="slug" required />
        </div>

        <div>
          <label htmlFor="version">Version:</label>
          <input type="text" id="version" name="version" placeholder="1.0.0" required />
        </div>

        <div>
          <label htmlFor="description">Description:</label>
          <textarea id="description" name="description" rows={4} required />
        </div>

        <div>
          <label htmlFor="extension_file">Extension File:</label>
          <input type="file" id="extension_file" name="extension_file" required />
        </div>

        <div>
          <label htmlFor="icon">Icon (optional):</label>
          <input type="file" id="icon" name="icon" accept="image/*" />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit Extension'}
        </button>
      </form>
    </div>
  );
}

export default SubmitExtensionPage;
