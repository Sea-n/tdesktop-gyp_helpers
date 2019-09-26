// This file is part of Desktop App Toolkit,
// a set of libraries for developing nice desktop applications.
//
// For license and copyright information please follow this link:
// https://github.com/desktop-app/legal/blob/master/LEGAL
//
#include <time.h>

#if defined(_M_X64) || defined(__x86_64__)
#define GETTIME_GLIBC_VERSION "2.2.5"
#elif defined(__aarch64__)
#define GETTIME_GLIBC_VERSION "2.17"
#else
#error Please add glibc wraps for your architecture
#endif

int __clock_gettime_glibc_old(clockid_t clk_id, struct timespec *tp);
__asm__(".symver __clock_gettime_glibc_old,clock_gettime@GLIBC_" GETTIME_GLIBC_VERSION);


int __wrap_clock_gettime(clockid_t clk_id, struct timespec *tp) {
        return __clock_gettime_glibc_old(clk_id, tp);
}

