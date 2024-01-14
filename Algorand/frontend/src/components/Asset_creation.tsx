import React from "react";

const trainees = [
  {
    id: 1,
    email: "elias.assamnew@gmail.com",
    full_name: "Elias Assamnew",
    address: "JMTMOM7GPPWXCOESP4AHOBUE3PW6HD7IR43GDDRTCYIEWJV4AGU6AOVTCE",
    status: "true",
    cid: "https://ipfs.io/ipfs/QmRkePdXa4F15Pr234imUR1knjDccWDSN4WgPjoivfd3vJ"
  },
  {
    id: 2,
    email: "user@gmail.com",
    full_name: "user user",
    address: "NEV4DYHHRHK4I4ZXA4VKBHAHYBIHGBQC56BDEM3T5NGW2BI4VAZ4PYH7FI",
    status: "false",
    cid: "https://ipfs.io/ipfs/QmRkePdXa4F15Pr234imUR1knjDccWDSN4WgPjoivfd3vJ"
  },
];

export default function CreateAsset() {
  async function copyToClipboard(clipboardText: string) {
    try {
      await navigator.clipboard.writeText(clipboardText);
      console.log("Text copied to clipboard");
    } catch (error) {
      console.error("Failed to copy text: ", error);
    }
  }

  return (
    <table className="min-w-full">
      <thead>
        <tr>
          <th className="w-[100px]">Id</th>
          <th>Email</th>
          <th>Full Name</th>
          <th className="text-right">Address</th>
          <th className="text-right">Status</th>
          <th className="text-right">ImageUrl</th>
          <th className="text-right">Create Assets</th>
        </tr>
      </thead>
      <tbody>
        {trainees.map((trainee) => (
          <tr key={trainee.id}>
            <td className="font-medium">{trainee.id}</td>
            <td>{trainee.email}</td>
            <td>{trainee.full_name}</td>
            <td className="text-right">{trainee.address.slice(0, 3)}...{trainee.address.slice(-3)}</td>
            <td className="text-right">{trainee.status}</td>
            <td className="text-right">{trainee.cid.slice(0, 5)}...{trainee.cid.slice(-5)}</td>
            <td className="text-right">
              <button onClick={() => copyToClipboard(trainee.cid)}>Create Asset</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
