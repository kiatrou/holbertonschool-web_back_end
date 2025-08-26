export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}

// ES6 introduced shorthand syntax for this pattern (when the keys and values have the exact same names). When the key name and variable name are identical, you can just write the name once
