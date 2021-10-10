module.exports = {
  purge: {
    enabled: true,
    content: ["./src/components/*.vue"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: "#8a0000",
        secondary: "#ffc420",
        creen: "#00E500",
      },
      outline: {
        red: "2px solid #8a0000",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
