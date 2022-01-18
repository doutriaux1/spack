# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyKosh(PythonPackage):
    """Kosh allows codes to store, query, share data via an easy-to-use Python API.
Kosh lies on top of Sina and as a result can use any database backend supported by Sina.
In adition Kosh aims to make data access and sharing as simple as possible.
"""

    homepage = "https://github.com/LLNL/kosh"
    git = "https://github.com/LLNL/kosh.git"

    # notify when the package is updated.
    maintainers = [
        'doutriaux1',
    ]
    version('2.0', sha256='059e431e3d3219b53956cb464d9e10933ca141dc89662f55d9c633e35c8b3a1e')

    depends_on('py-setuptools', type='build')
    depends_on("py-llnl-sina", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
