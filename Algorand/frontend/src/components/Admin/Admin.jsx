import React from 'react'

const Admin = () => {
  const handleTransferAsset = () => {
    // Add logic for transferring assets here
  }

  return (
    <div>
      <h1>Admin</h1>
      <button onClick={handleTransferAsset} style={{ backgroundColor: 'red', color: 'white' }}>
        Transfer Asset
      </button>
    </div>
  )
}

export default Admin
