

# def sign_in(request):
#     if not request.method == 'POST':
#         return JsonResponse({settings.ERROR_MESSAGE_KEY: "Invalid method"}, status=405)

#     phone = clean_phone(request.json.get('phone'))
#     password = request.json.get('password')
#     device_token = request.json.get('deviceToken')

#     none_field_idx = -1
#     try:
#         none_field_idx = (phone, password).index(None)
#     except ValueError:
#         pass

#     if none_field_idx >= 0:
#         required_fields = ('phone', 'password')
#         error_result = {"msg": f"Missing required field: \"{required_fields[none_field_idx]}\""}
#         return JsonResponse(error_result, status=400)

#     user = authenticate(request, phone=phone, password=password)
#     if user:
#         if not (user.is_store_owner or user.is_superuser) and user.phone_auth is None:
#             return JsonResponse({settings.ERROR_MESSAGE_KEY: "전화번호 인증을 받지 않았습니다. 고객센터로 문의해 주세요."}, status=401)
#         access_token = create_access_token(user)
#     else:
#         error_result = {
#             settings.ERROR_MESSAGE_KEY: "전화번호, 혹은 비밀번호가 일치하지 않습니다."
#         }
#         return JsonResponse(error_result, status=401)

#     if device_token:
#         user.device_token = device_token
#     user.save()

#     result = {"accessToken": access_token, "userUUID": user.uuid}

#     try:
#         Store.objects.get(owner=user)
#     except Store.DoesNotExist:
#         return JsonResponse(result)

#     result["storeUUID"] = user.store.uuid
#     return JsonResponse(result)
