import { Client, Databases, ID } from 'appwrite';
import fs from 'fs';
import path from 'path';

const client = new Client()
    .setEndpoint('https://fra.cloud.appwrite.io/v1') // e.g., 'https://cloud.appwrite.io/v1'
    .setProject('684887f70039f5d9e06a')
    .setKey('standard_bb25d1ed6e63940903c57e9bde52890e2f2d77146819a343b023da3645447e16f4974059da6e7d3e2f86aa8d4804fdece1504bfc087631af9b9ed829961f8665eee4a07c42146cc9ef41c32c36014c4eef50556a78c0e8c766f8e5dbd8c3306b970dcc79e88a1a9928e5c8a7699c14072aadebb5ef19697535f84e0f3ceed91d'); // Server-side API key with write permissions

const databases = new Databases(client);

const databaseId = 'YOUR_DATABASE_ID'; // e.g., 'ConversationData'
const collectionId = 'YOUR_COLLECTION_ID'; // e.g., 'Scenarios'
const scenariosDir = './scenarios'; // Path to your JSON files

async function uploadScenarios() {
    try {
        const files = fs.readdirSync(scenariosDir);
        for (const file of files) {
            if (file.endsWith('.json')) {
                const filePath = path.join(scenariosDir, file);
                const rawData = fs.readFileSync(filePath, 'utf-8');
                const jsonData = JSON.parse(rawData);

                // Handle JSON with a list of conversations
                const conversations = jsonData.conversations || (Array.isArray(jsonData) ? jsonData : [jsonData]);

                for (const scenarioData of conversations) {
                    // Standardize fields
                    scenarioData.cultural_notes = scenarioData.cultural_notes || scenarioData.cultural_elements || [];
                    scenarioData.friendship_factor = scenarioData.friendship_factor || 'none';
                    scenarioData.friendship_progression = scenarioData.friendship_progression || 'none';
                    delete scenarioData.cultural_elements; // Remove old field

                    await databases.createDocument(
                        databaseId,
                        collectionId,
                        scenarioData.scenario_id || ID.unique(), // Use scenario_id or generate unique ID
                        scenarioData
                    );
                    console.log(`Uploaded scenario: ${scenarioData.scenario_id}`);
                }
            }
        }
        console.log('All scenarios uploaded successfully.');
    } catch (error) {
        console.error('Error uploading scenarios:', error.message);
    }
}

uploadScenarios();