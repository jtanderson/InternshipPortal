module.exports = {
  purge: {
    enabled: true,
    content: ["./src/components/*.vue", "./src/pages/*.vue"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: "#8a0000",
        primaryOffset: "#b41717",
        secondary: "#ffc420",
        creen: "#00E500",
      },
      outline: {
        red: "2px solid #8a0000",
      },
      flex: {
        df: "0 1 auto",
        el: "0 0 50%",
        ef: "0 0 100%",
        nm: "1 1 100%",
        sm: "1 1 100%",
        md: "1 1 32%",
        lg: "1 1 32%",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
