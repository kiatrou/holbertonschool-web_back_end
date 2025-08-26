function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
  [`income-${getCurrentYear()}`]: income,
  [`gdp-${getCurrentYear()}`]: gdp,
  [`capita-${getCurrentYear()}`]: capita,
  };

  return budget;
}

// this is using computed propery names. This allows you to use expressions inside square brackets [...] to dynamically create property keys when defining an object literal
