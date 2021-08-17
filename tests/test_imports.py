"""
Tests to ensure that all imports work properly
"""


def test_main():
    from perm_security import Token, validate

    assert isinstance(Token, type)
    assert callable(validate)


def test_member_adapter():
    from perm_security.MemberAdapter import MemberAdapter, MemberChannelAdapter, MemberGuildAdapter

    assert isinstance(MemberAdapter, type)
    assert isinstance(MemberChannelAdapter, type)
    assert isinstance(MemberGuildAdapter, type)


def test_permissions():
    from perm_security.Permission import (
        GuildPermissions,
        StageChannelPermissions,
        TextChannelPermissions,
        VoiceChannelPermissions,
    )

    assert isinstance(GuildPermissions, type)
    assert isinstance(StageChannelPermissions, type)
    assert isinstance(TextChannelPermissions, type)
    assert isinstance(VoiceChannelPermissions, type)


def test_token_strategy():
    from perm_security.TokenStrategy import (
        TokenStrategy,
        BasicTokenStrategy,
        MismatchPermissionException,
        NonMemberTokenException,
        PermissionDeniedException,
    )

    assert isinstance(TokenStrategy, type)
    assert isinstance(BasicTokenStrategy, type)
    assert isinstance(MismatchPermissionException, type)
    assert isinstance(NonMemberTokenException, type)
    assert isinstance(PermissionDeniedException, type)


def test_token_handler_strategy():
    from perm_security.TokenStrategy.TokenHandlerStrategy import TokenHandlerStrategy, BasicTokenHandlerStrategy

    assert isinstance(TokenHandlerStrategy, type)
    assert isinstance(BasicTokenHandlerStrategy, type)
