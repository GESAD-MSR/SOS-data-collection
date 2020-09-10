module.exports = {
  purge: {
    enabled: false,
    content: ["./src/**/*.html", "./src/**/*.vue"]
  },
  theme: {
    extend: {}
  },
  variants: {
    borderColor: ["responsive", "hover", "active", "focus"]
  },
  plugins: []
};
