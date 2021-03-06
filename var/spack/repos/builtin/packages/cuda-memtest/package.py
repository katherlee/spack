##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class CudaMemtest(CMakePackage):
    """Maintained and updated fork of cuda_memtest.

    original homepage: http://sourceforge.net/projects/cudagpumemtest .

    This software tests GPU memory for hardware errors and soft errors
    using CUDA or OpenCL.
    """

    homepage = "https://github.com/ComputationalRadiationPhysics/cuda_memtest"
    url      = "https://github.com/ComputationalRadiationPhysics/cuda_memtest.git"

    version('master', branch='dev',
            git='https://github.com/ComputationalRadiationPhysics/cuda_memtest.git')

    depends_on('cmake@2.8.5:', type='build')
    # depends_on('nvml', when='+nvml')
    depends_on('cuda@5.0:')
