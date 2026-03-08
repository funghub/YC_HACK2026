'use server';

import { action } from "./_generated/server";
import { v } from "convex/values";

export const submitJob = action({
  args: {
    proteinFileContent: v.string(),
    ligandFileContent: v.string(),
  },
  handler: async (ctx, args) => {
    const apiKey = process.env.TAMARIND_API_KEY;

    if (!apiKey) {
      throw new Error("Tamarind API key is not set in environment variables.");
    }

    const response = await fetch("https://app.tamarind.bio/api/submit-job", {
      method: "POST",
      headers: {
        "x-api-key": apiKey,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        jobName: "bio-ai-analysis",
        type: "drugflow",
        settings: {
          pdbFile: args.proteinFileContent,
          referenceLigandFile: args.ligandFileContent,
          numSamples: 5,
          numBatches: 1,
          distCutoff: 8,
        },
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Tamarind API request failed: ${errorText}`);
    }

    return await response.json();
  },
});
