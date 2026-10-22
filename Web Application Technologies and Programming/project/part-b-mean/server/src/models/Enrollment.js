import mongoose from 'mongoose';

const enrollmentSchema = new mongoose.Schema(
  {
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    email: { type: String, required: true },
    password: { type: String, required: true }, 
    level: { type: String, enum: ['beginner', 'intermediate', 'advanced'], required: true },
    categories: [{ type: String }],
    courses: [{ type: String }]
  },
  { timestamps: true }
);

const Enrollment = mongoose.model('Enrollment', enrollmentSchema);
export default Enrollment;
