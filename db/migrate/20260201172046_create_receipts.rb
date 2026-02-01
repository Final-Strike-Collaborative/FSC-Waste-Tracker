class CreateReceipts < ActiveRecord::Migration[8.1]
  def change
    create_table :receipts do |t|
      t.string :note
      t.decimal :grand_total, precision: 24, scale: 2

      t.timestamps
    end
  end
end
