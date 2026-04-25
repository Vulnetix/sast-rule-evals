# Sample for Ruff rule PYI034: non-self-return-type
# This file is designed to trigger the PYI034 rule.
# Run: ruff check --select PYI034 <this_file>

class Shape:
    def set_scale(self, scale: float) -> Shape:
        self.scale = scale
        return self

class Circle(Shape):
    def set_radius(self, radius: float) -> Circle:
        self.radius = radius
        return self

# Type checker infers return type as `Shape`, not `Circle`.
Circle().set_scale(0.5)

# Thus, this expression is invalid, as `Shape` has no attribute `set_radius`.
Circle().set_scale(0.5).set_radius(2.7)
