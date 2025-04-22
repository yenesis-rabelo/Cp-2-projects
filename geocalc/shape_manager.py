def sort_shapes(shapes, key='area'):
    if key == 'area':
        return sorted(shapes, key=lambda s: s.area())
    elif key == 'perimeter':
        return sorted(shapes, key=lambda s: s.perimeter())
    else:
        raise ValueError("Sort key must be 'area' or 'perimeter'.")
