import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import MarketplacePage from './pages/MarketplacePage'
import './App.css'

function App() {
  return (
    <Router>
      <div className="app">
        <nav className="navbar">
          <h1>Extensions Marketplace</h1>
          <div className="nav-links">
            <Link to="/">Marketplace</Link>
            <Link to="/submit">Submit Extension</Link>
            <Link to="/reviewer">Reviewer Dashboard</Link>
          </div>
        </nav>
        <main className="content">
          <Routes>
            <Route path="/" element={<MarketplacePage />} />
            <Route path="/submit" element={<SubmitExtensionPage />} />
            <Route path="/reviewer" element={<ReviewerDashboardPage />} />
            <Route path="/extension/:id" element={<ExtensionDetailPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

function SubmitExtensionPage() {
  return <div><h2>Submit Extension</h2><p>Developer submission form</p></div>;
}

function ReviewerDashboardPage() {
  return <div><h2>Reviewer Dashboard</h2><p>Review pending extensions</p></div>;
}

function ExtensionDetailPage() {
  return <div><h2>Extension Details</h2><p>View single extension</p></div>;
}

export default App;
