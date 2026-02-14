import { useEffect, useState } from 'react';

export default function Home() {
  const [health, setHealth] = useState<{status: string, service: string} | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealth(data))
      .catch(err => setError('Failed to connect to backend'));
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">Knowledge Graph Builder</h1>
      
      <div className="p-6 border rounded-lg bg-gray-50 dark:bg-gray-900 max-w-sm w-full">
        <h2 className="text-xl font-semibold mb-4">System Status</h2>
        
        {error ? (
          <div className="text-red-500">❌ {error}</div>
        ) : health ? (
          <div className="space-y-2">
            <div className="flex justify-between">
              <span>API Status:</span>
              <span className="text-green-600 font-bold">{health.status}</span>
            </div>
            <div className="flex justify-between">
              <span>Service:</span>
              <span className="text-blue-600">{health.service}</span>
            </div>
          </div>
        ) : (
          <div className="text-gray-500 animate-pulse">Connecting to backend...</div>
        )}
      </div>
    </main>
  );
}