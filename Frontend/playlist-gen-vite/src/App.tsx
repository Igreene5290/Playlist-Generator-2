import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home.tsx'

function App() {

  return (
    <Routes>
      <Route path="/" element={
        <div className="App">
          <p className="title">Playlist Generator</p>
          <div className="card">
            <button onClick={() => window.location.href = '/api/login'}>
              Log in with Spotify
            </button>
          </div>
        </div>
      } />
      <Route path="/home" element={<Home />} />
    </Routes>
  );
}

export default App
