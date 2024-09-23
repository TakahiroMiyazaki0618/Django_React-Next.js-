"use client";

import React from "react";

export default function Page() {
  const showDialog: any = () => {
    alert("アラート");
  };

  return (
    <div>
      <button onClick={showDialog()}>Click</button>
    </div>
  );
}
