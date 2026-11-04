# Software environment of the ATLAS Open Data ADL Analysis Suite.
#
# The image holds the software only: ROOT 6.30.02, CutLang v2.16.0 and the Open Data framework
# fork (release 10fb-legacy-validation-v1), plus the Python packages of the suite scripts.
# The suite itself is mounted at run time (see the README, "Running in the container"), so the
# image digest does not change with the suite's files.
#
# Build (from the repository root):
#   docker buildx build --platform linux/amd64 -t adl4atlasopendata-env:1.0.0 docker/

# Official ROOT 6.30.02 image on AlmaLinux 9, pinned by digest (amd64 only)
FROM rootproject/root:6.30.02-alma9@sha256:bfaf5e4c49e85eb9d79685a7f27a4b00f5b436d4d66144e96898933c7d627a7f

# Releases used, checked out by tag; the build stops if a tag no longer points to its commit
ARG CUTLANG_TAG=v2.16.0
ARG CUTLANG_COMMIT=1f880fc99da1e8d9240c5d62dc733c59ca2c4608
ARG OPENDATA_FRAMEWORK_TAG=10fb-legacy-validation-v1
ARG OPENDATA_FRAMEWORK_COMMIT=2c039ff984316f980728b0a58a5f492126ca574d
ARG BISON_VERSION=3.8.2
ARG BISON_SHA256=9bba0214ccf7f1079c5d59210045227bcf619519840ebfa80cd3849cff5a5bf2

# Build tools; flex from AlmaLinux 9 (2.6.4)
RUN dnf install -y git make gcc-c++ flex m4 xz wget which python3-pip && dnf clean all

# bison 3.8.2, the version used for the reference CutLang build
# (MAKEINFO=true: the manual is not rebuilt, as makeinfo is not installed)
RUN cd /tmp && wget -q https://ftp.gnu.org/gnu/bison/bison-${BISON_VERSION}.tar.xz \
 && echo "${BISON_SHA256}  bison-${BISON_VERSION}.tar.xz" | sha256sum -c - \
 && tar xf bison-${BISON_VERSION}.tar.xz && cd bison-${BISON_VERSION} \
 && ./configure --prefix=/usr/local -q \
 && make -j"$(nproc)" -s MAKEINFO=true && make install -s MAKEINFO=true \
 && cd /tmp && rm -rf bison-${BISON_VERSION}*

# Python packages of the suite scripts, with all dependencies pinned
COPY requirements.lock /tmp/requirements.lock
RUN python3 -m pip install --no-cache-dir --no-deps -r /tmp/requirements.lock

# CutLang v2.16.0
RUN git clone https://github.com/unelg/CutLang.git /opt/CutLang \
 && cd /opt/CutLang && git checkout -q tags/${CUTLANG_TAG} \
 && test "$(git rev-parse HEAD)" = "${CUTLANG_COMMIT}" \
 && cd CLA && make -s -j"$(nproc)" \
 && chmod -R a+rwX /opt/CutLang
ENV CUTLANG_DIR=/opt/CutLang
ENV PATH=/opt/CutLang/runs:${PATH}

# ATLAS Open Data framework fork used for the validation (needs ROOT and the compiler at run time)
RUN git clone https://github.com/ahmetcansansar/atlas-outreach-cpp-framework-13tev.git /opt/atlas-outreach-cpp-framework-13tev \
 && cd /opt/atlas-outreach-cpp-framework-13tev && git checkout -q tags/${OPENDATA_FRAMEWORK_TAG} \
 && test "$(git rev-parse HEAD)" = "${OPENDATA_FRAMEWORK_COMMIT}" \
 && chmod -R a+rwX /opt/atlas-outreach-cpp-framework-13tev
ENV OPENDATA_FRAMEWORK_DIR=/opt/atlas-outreach-cpp-framework-13tev

LABEL org.opencontainers.image.title="ATLAS Open Data ADL Benchmark Suite environment" \
      org.opencontainers.image.source="https://github.com/ahmetcansansar/ADL4ATLASOpenData" \
      org.opencontainers.image.licenses="MIT"

# The suite is mounted at /work; by default the reduced benchmark runs
WORKDIR /work
CMD ["python3", "scripts/reduced_benchmark.py"]
