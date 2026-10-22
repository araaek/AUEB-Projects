export function notImplemented(req, res) {
  res.status(501).json({ message: "Δεν το έχουμε υλοποιήσει. Για μελλοντική χρήση!!!" });
}
