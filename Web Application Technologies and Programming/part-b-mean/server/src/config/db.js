// src/config/db.js

import mongoose from "mongoose";

export async function connectDB(mongoUri) {
  try {
    // Προσπάθεια σύνδεσης στη MongoDB
    await mongoose.connect(mongoUri, {
    
    });

    console.log("[DB] Connected to MongoDB");
  } catch (err) {
    console.error("[DB] Connection error:", err.message);

    
    throw err; // το αφήνω ώστε ο app.js να χειριστεί το σφάλμα
  }
}
