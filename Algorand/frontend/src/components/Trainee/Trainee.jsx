import React from 'react'

const Admin = () => {
  const handleOPTAsset = () => {
    // Add logic for transferring assets here
  }

  return (
    <div>
      <h1>Admin</h1>
      <button onClick={handleOPTAsset} style={{ backgroundColor: 'green', color: 'white' }}>
        OPT Asset
      </button>
    </div>
  )
}

export default Admin
