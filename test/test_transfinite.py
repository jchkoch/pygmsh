import pygmsh


def test(lcar=1.0):
    geom = pygmsh.built_in.Geometry()
    poly = geom.add_polygon(
        [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]], lcar
    )

    geom.set_transfinite_surface(poly.surface, size=[11, 9])

    mesh = pygmsh.generate_mesh(geom, geo_filename="transfinite.geo")
    assert len(mesh.cells_dict["triangle"]) == 10 * 8 * 2
    return mesh


if __name__ == "__main__":
    import meshio

    meshio.write("transfinite.vtu", test())
