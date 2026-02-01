class Material < ApplicationRecord
  enum :unit_of_measure, {
    pounds: "lbs",
    ounces: "oz",
    boardfeet: "bdft",
    count: "count",
    feet: "feet"
  }
end
