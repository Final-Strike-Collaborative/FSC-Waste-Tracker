class CreateMaterials < ActiveRecord::Migration[8.1]
  def change
    create_table :materials do |t|
      t.decimal :quantity, precision: 24, scale: 2
      t.decimal :price, precision: 24, scale: 2
      t.string :unit_of_measure
      t.string :note

      t.timestamps
    end
  end
end
