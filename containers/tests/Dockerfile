FROM python:3.7

# Install pyiqfeed
RUN git clone https://github.com/akapur/pyiqfeed.git && \
    cd pyiqfeed && \
    git checkout ec98776b157857a8c141c4d452245282c5ede764 && \
    python3 setup.py install && \
    cd .. && rm -rf pyiqfeed

# Install pytest
RUN pip install pytest==4.3.1

# Set up tini
COPY --from=tiemensch/tiniconda:ubuntu-bionic /usr/local/bin/tini /usr/local/bin/tini
ENTRYPOINT ["/usr/local/bin/tini", "--"]

# Copy source code
COPY tests /apps/tests
CMD ["pytest", "/apps/tests"]
