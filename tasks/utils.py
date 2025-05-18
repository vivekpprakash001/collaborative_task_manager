def queryset_to_dict_list(queryset):
    dict_list = []
    for obj in queryset:
        # Using model's _meta to get field names dynamically
        fields = [field.name for field in obj._meta.fields]

        obj_dict = {field: getattr(obj, field) for field in fields}
        dict_list.append(obj_dict)
    return dict_list
