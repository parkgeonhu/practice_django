    
def _order_name(item_names: list):
    if len(item_names) > 1:
        return f'{item_names[0]} 외 {len(item_names) - 1}건'
    else:
        return item_names[0]

def make_order():
    #_order_name으로 Order 객체 만들어주고
    
    #orderItem 유효성 체크
    
    #결제가 되면 orderItem 만들어줌
    
    pass
    
      
# orderitem으로 넘겨주는 함수    
def make_orderItem(store: Store, order: Order, order_items: list):
    item_names = []
    for item in order_items:
        product = Product.objects.filter(uuid=item.get('productUUID'), is_available=True).first()
        if product is None or product.store != store:
            raise RequestSanityException("잘못된 상품이 선택되었습니다.")
        grand_total_from_db += product.default_price
        item_names.append(product.name)

        options = item.get('options', [])

        """
        options = [
            {"name": "사이즈", "value": "사이즈업", "additionalPrice": 1000},
            {"name": "HOT/ICE", "value": "ICE", "additionalPrice": 500},
            {"name": "샷 추가", "value": "3", "additionalPrice": 300},
            {"name": "세트메뉴", "value": ["머핀", "치즈케잌"], "additionalPrice": 4400},
        ]
        """
        for option in options:
            product_option = next(filter(lambda po: po["name"] == option["name"], product.options))
            """
            product.options = [
                {
                    "name": "사이즈",
                    "type": "RADIO",
                    "availableOptions": [
                        { "value": "기본", "additionalPrice": 0},
                        { "value": "사이즈업", "additionalPrice": 1000 }
                    ]
                }, {
                    "name": "HOT/ICE",
                    "type": "RADIO",
                    "availableOptions": [
                        { "value": "HOT", "additionalPrice": 0 },
                        { "value": "ICE", "additionalPrice": 500 }
                    ]
                }, {
                    "max": 5,
                    "name": "샷 추가",
                    "type": "COUNTABLE",
                    "additionalPrice": 100
                }, {
                    "name": "세트메뉴",
                    "type": "CHECKBOX",
                    "availableOptions": [
                        { "value": "머핀", "additionalPrice": 1700 },
                        { "value": "치즈케잌", "additionalPrice": 2700 },
                        { "value": "롤케잌", "additionalPrice": 5000 },
                    ],
                    "max": 2  // 최대 선택 가능한 옵션 갯수
                },
            ]
            """
            option["type"] = product_option["type"]
            if product_option["type"] == "COUNTABLE":
                shot_cnt = int(option["value"])
                grand_total_from_db += product_option["additionalPrice"] * abs(shot_cnt)
                # prevent multiply minus
            elif product_option["type"] == "CHECKBOX":
                selections = option["value"]
                if type(selections) is not list:
                    raise RequestSanityException("잘못된 형식의 옵션이 지정되었습니다.", code=400)
                if len(selections) > product_option["max"]:
                    raise RequestSanityException(f"{option['name']} 선택 가능 개수를 초과했습니다.", code=400)
                for opt in product_option["availableOptions"]:
                    if opt["value"] in selections:
                        grand_total_from_db += opt["additionalPrice"]
            else:
                selected_option = next(
                    filter(lambda a: a["value"] == option["value"], product_option["availableOptions"])
                )
                grand_total_from_db += int(selected_option["additionalPrice"])

        OrderItem.objects.create(product=product, options=options, order=order)
        
    return render(request, 'blog/signup.html', {'form': form})

    