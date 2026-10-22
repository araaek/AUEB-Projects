import "dotenv/config";
import express from "express";
import cors from "cors";

import mongoose from 'mongoose';


// Σύνδεση βάσης
import { connectDB } from "./config/db.js";

// Routes
import coursesRouter from "./routes/courses.routes.js";

// Εγγραφή μαθητών
import enrollmentsRoutes from './routes/enrollments.routes.js';

// Error handler
import { errorHandler } from "./middleware/errorHandler.js";

const app = express();

// --- Middlewares ---
app.use(cors());
app.use(express.json());


// No-cache headers ΜΟΝΟ για API
app.set("etag", false);

app.use("/api", (req, res, next) => {
  res.set("Cache-Control", "no-store, no-cache, must-revalidate, proxy-revalidate");
  res.set("Pragma", "no-cache");
  res.set("Expires", "0");
  res.set("Surrogate-Control", "no-store");
  next();
});


// --- Routes ---
app.use("/api/courses", coursesRouter);
app.use('/api/enrollments', enrollmentsRoutes);

// Health check
app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});

// Error handler 
app.use(errorHandler);


// --- Εκκίνηση Server + Database ---
const PORT = process.env.PORT || 4000;
const MONGO_URI = process.env.MONGODB_URI;

async function start() {
  try {
    await connectDB(MONGO_URI);

    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
    });

  } catch (err) {
    console.error("Failed to start server:", err);
  }
}


app.listen(4000, () => {
  console.log('Server listening on port 4000');
});
start();