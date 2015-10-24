
#  Copyright 2005 Red Hat, Inc.
#
#  Permission to use, copy, modify, distribute, and sell this software and its
#  documentation for any purpose is hereby granted without fee, provided that
#  the above copyright notice appear in all copies and that both that
#  copyright notice and this permission notice appear in supporting
#  documentation, and that the name of Red Hat not be used in
#  advertising or publicity pertaining to distribution of the software without
#  specific, written prior permission.  Red Hat makes no
#  representations about the suitability of this software for any purpose.  It
#  is provided "as is" without express or implied warranty.
#
#  RED HAT DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
#  INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
#  EVENT SHALL RED HAT BE LIABLE FOR ANY SPECIAL, INDIRECT OR
#  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
#  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
#  TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
#  PERFORMANCE OF THIS SOFTWARE.
#

# Initialize Autoconf
AC_PREREQ([2.60])
AC_INIT([libXtst], [1.2.2],
	[https://bugs.freedesktop.org/enter_bug.cgi?product=xorg], [libXtst])
AC_CONFIG_SRCDIR([Makefile.am])
AC_CONFIG_HEADERS([config.h])

# Initialize Automake
AM_INIT_AUTOMAKE([foreign dist-bzip2])

# Initialize libtool
AC_PROG_LIBTOOL

# Require xorg-macros minimum of 1.12 for DocBook external references
m4_ifndef([XORG_MACROS_VERSION],
          [m4_fatal([must install xorg-macros 1.12 or later before running autoconf/autogen])])
XORG_MACROS_VERSION(1.12)
XORG_DEFAULT_OPTIONS
XORG_ENABLE_SPECS
XORG_WITH_XMLTO(0.0.22)
XORG_WITH_FOP
XORG_WITH_XSLTPROC
XORG_CHECK_SGML_DOCTOOLS(1.8)

# Obtain compiler/linker options for depedencies
PKG_CHECK_MODULES(XTST, x11 [xext >= 1.0.99.4] xi [recordproto >= 1.13.99.1] [xextproto >= 7.0.99.3] inputproto)

# Check for _XEatDataWords function that may be patched into older Xlib release
SAVE_LIBS="$LIBS"
LIBS="$XTST_LIBS"
AC_CHECK_FUNCS([_XEatDataWords])
LIBS="$SAVE_LIBS"

# Check for support XTest Touch EVENT
AC_ARG_ENABLE(xtest-touch, AS_HELP_STRING([--enable-xtest-touch], [Enable X Test Touch* functions (default: disabled)]), [XTESTTOUCH=$enableval],[XTESTTOUCH=no])
if test "x$XTESTTOUCH" == xyes; then
	XTESTTOUCH_CFLAGS="-D_F_SUPPORT_XTEST_TOUCH_EVENT_ "
	AC_SUBST(XTESTTOUCH_CFLAGS)
fi

# Check for privilege check is enabled
AC_ARG_ENABLE(privilege-check-on-xtest-device-api, AS_HELP_STRING([--enable-privilege-check-on-xtest-device-api], [Enable X Test privilege check (default: disabled)]), [ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API=$enableval],[ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API=no])
if test "x$ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API" == xyes; then
	ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API_CFLAGS="-D_ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API_ "
	AC_SUBST(ENABLE_PRIVILEGE_CHECK_ON_XTEST_DEVICE_API_CFLAGS)
fi

# Determine if the source for man pages is available
# It may already be present (tarball) or can be generated using xmlto
AM_CONDITIONAL([INSTALL_MANPAGES],
	[test -f "$srcdir/man/XTestQueryExtension.man" || test "x$have_xmlto" = xyes])

# Allow checking code with lint, sparse, etc.
XORG_WITH_LINT
XORG_LINT_LIBRARY([Xtst])
LINT_FLAGS="${LINT_FLAGS} ${XTST_CFLAGS}"

AC_CONFIG_FILES([Makefile
		man/Makefile
		src/Makefile
		specs/Makefile
		xtst.pc])
AC_OUTPUT
