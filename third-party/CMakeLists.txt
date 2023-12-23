
include(ExternalProject)

# Set up an external project to pull source code from Git along with submodules
ExternalProject_Add(
    dbcppp# Name for this external project
    PREFIX ${CMAKE_BINARY_DIR}/external/dbcppp  # Directory where the source will be downloaded
    GIT_REPOSITORY https://github.com/xR3b0rn/dbcppp.git  # Replace with your Git repository URL
    GIT_TAG v3.2.6 # Replace with the branch or tag you want to use
    TIMEOUT 10  # Adjust as needed
    CONFIGURE_COMMAND ""  # No configuration needed
    BUILD_COMMAND ""  # No build commands needed
    INSTALL_COMMAND ""  # No installation needed
    LOG_DOWNLOAD ON  # Enable logging for download details
    GIT_SUBMODULES_INIT ON  # Fetch submodules
)

# Use the downloaded project as part of your build
ExternalProject_Get_Property(dbcppp source_dir)
add_subdirectory(${source_dir} ${CMAKE_BINARY_DIR}/external/dbcppp-build)

# Enable CPack module
include(CPack)

# Set the basic CPack settings
set(CPACK_GENERATOR "NSIS")  # Use NSIS installer (you can use other generators as needed)
set(CPACK_PACKAGE_NAME "dbcppp")
set(CPACK_PACKAGE_VERSION "3.2.6")
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")

# Specify files to be installed (your executable and any other necessary files)
install(TARGETS dbcppp DESTINATION bin)  # Replace YourExecutable with your actual target name

# Other installation instructions for additional files, if any

