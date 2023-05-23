/*
        data = {
            "name": request.data.get("name", product.name),
            "description": request.data.get("description", product.description),
            "price": request.data.get("price", product.price),
            "discount": request.data.get("discount", product.discount),
            "Category": request.data.get("Category", product.Category.id),
            "dealer": request.data.get("Category", product.dealer.id),
        }

*/

export interface IProduct{
    name: string;
    description: string;
    price: number;
    discount: number;
    category: number;
    dealer: number;
}
